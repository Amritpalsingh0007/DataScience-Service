from pydantic import BaseModel, Field
from typing import Optional

class Expense (BaseModel):
    amount: Optional[int] = Field(title="expense", description="expense made in the transaction")
    merchant: Optional[str] = Field(title="merchant", description="merchant name whom the transaction has been made")
    currency: Optional[str] = Field(title="currency", description="currency of transaction")