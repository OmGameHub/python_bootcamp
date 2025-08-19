from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None

Comment.model_rebuild()

comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2", replies=[
            Comment(id=4, content="nested reply 1"),
            Comment(id=5, content="nested reply 2")
        ]),
    ]
)
print(comment)