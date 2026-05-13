import json

from datasets import Dataset

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)

from peft import (
    LoraConfig,
    get_peft_model
)

# =========================
# LOAD DATASET
# =========================

with open(
    "app/ml/lora/dataset.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

# =========================
# FORMAT DATA
# =========================

formatted_data = []

for item in data:

    text = f"""
### Instruction:
{item['instruction']}

### Response:
{item['response']}
"""

    formatted_data.append({
        "text": text
    })

dataset = Dataset.from_list(formatted_data)

# =========================
# LOAD MODEL
# =========================

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name)

# =========================
# TOKENIZE
# =========================

def tokenize(example):

    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=256
    )

tokenized_dataset = dataset.map(tokenize)

# =========================
# LORA CONFIG
# =========================

config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)

# =========================
# TRAINING ARGS
# =========================

training_args = TrainingArguments(
    output_dir="app/ml/lora/output",
    per_device_train_batch_size=1,
    num_train_epochs=1,
    logging_steps=1,
    save_steps=10
)

# =========================
# TRAINER
# =========================

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )
)

# =========================
# TRAIN
# =========================

trainer.train()

# =========================
# SAVE MODEL
# =========================

model.save_pretrained(
    "app/ml/lora/adapter"
)

print("LoRA training complete")