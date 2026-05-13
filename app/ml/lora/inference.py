from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer
)

from peft import PeftModel

# =========================
# LOAD BASE MODEL
# =========================

base_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-0.5B-Instruct"
)

tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2.5-0.5B-Instruct"
)

# =========================
# LOAD LORA ADAPTER
# =========================

model = PeftModel.from_pretrained(
    base_model,
    "app/ml/lora/adapter"
)

# =========================
# QUESTION
# =========================

question = """
### Instruction:
Как получить общежитие?

### Response:
"""

inputs = tokenizer(
    question,
    return_tensors="pt"
)

output = model.generate(
    **inputs,
    max_new_tokens=100,
    temperature=0.3,
    do_sample=True
)

response = tokenizer.decode(
    output[0],
    skip_special_tokens=True
)

print(response)