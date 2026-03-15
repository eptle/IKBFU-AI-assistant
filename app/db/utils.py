from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_or_create(db: AsyncSession, model, defaults=None, **kwargs):
    result = await db.execute(
        select(model).filter_by(**kwargs)
    )

    instance = result.scalar_one_or_none()

    if instance:
        return instance, False

    params = dict(kwargs)

    if defaults:
        params.update(defaults)

    instance = model(**params)

    db.add(instance)

    await db.commit()
    await db.refresh(instance)

    return instance, True