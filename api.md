# Chat

Types:

```python
from premai.types import ChatCompletionsResponse
```

Methods:

- <code title="post /api/v1/chat/completions">client.chat.<a href="./src/premai/resources/chat.py">completions</a>(\*\*<a href="src/premai/types/chat_completions_params.py">params</a>) -> <a href="./src/premai/types/chat_completions_response.py">ChatCompletionsResponse</a></code>

# Models

Types:

```python
from premai.types import ModelListResponse, ModelListInternalResponse
```

Methods:

- <code title="get /api/internal/chat/models">client.models.<a href="./src/premai/resources/models.py">list</a>() -> <a href="./src/premai/types/model_list_response.py">ModelListResponse</a></code>
- <code title="get /api/internal/chat/internalModels">client.models.<a href="./src/premai/resources/models.py">list_internal</a>() -> <a href="./src/premai/types/model_list_internal_response.py">object</a></code>
