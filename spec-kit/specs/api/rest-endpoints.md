# API Specification: Task REST Endpoints

**Component**: Backend API (FastAPI)
**Phase**: II (Full-Stack Web App)
**Source**: `speckit.specify` (TR-006, TR-007)
**Status**: Draft

## Base Path

`/api/{user_id}/tasks`

**Note**: The `{user_id}` in the path should correspond to the authenticated user making the request. The backend MUST verify that the `{user_id}` in the path matches the `user_id` extracted from the JWT token for authorization (TR-007).

## Endpoints

### 1. `GET /api/{user_id}/tasks` - Retrieve All Tasks for a User

**Description**: Retrieves a list of all tasks belonging to the authenticated user.
**Authentication**: Required (JWT)
**Authorization**: User must be authenticated and the `{user_id}` in the path must match the authenticated user's ID.
**Request**:
-   **Method**: `GET`
-   **Headers**:
    -   `Authorization: Bearer <JWT_TOKEN>`
**Response**:
-   **Status 200 OK**:
    ```json
    [
        {
            "id": "uuid-of-task-1",
            "description": "Buy groceries",
            "status": "Pending",
            "created_at": "2026-02-22T10:00:00Z",
            "updated_at": "2026-02-22T10:00:00Z"
        },
        {
            "id": "uuid-of-task-2",
            "description": "Walk the dog",
            "status": "Complete",
            "created_at": "2026-02-22T09:00:00Z",
            "updated_at": "2026-02-22T11:00:00Z"
        }
    ]
    ```
-   **Status 401 Unauthorized**: If JWT is missing or invalid.
-   **Status 403 Forbidden**: If `{user_id}` in path does not match authenticated user.
-   **Status 500 Internal Server Error**: For unexpected server issues.

---

### 2. `GET /api/{user_id}/tasks/{task_id}` - Retrieve a Specific Task for a User

**Description**: Retrieves a single task belonging to the authenticated user by its ID.
**Authentication**: Required (JWT)
**Authorization**: User must be authenticated and the `{user_id}` in the path must match the authenticated user's ID. The `task_id` must belong to the authenticated user.
**Request**:
-   **Method**: `GET`
-   **Path Parameters**:
    -   `task_id` (UUID): The unique identifier of the task.
-   **Headers**:
    -   `Authorization: Bearer <JWT_TOKEN>`
**Response**:
-   **Status 200 OK**:
    ```json
    {
        "id": "uuid-of-task-1",
        "description": "Buy groceries",
        "status": "Pending",
        "created_at": "2026-02-22T10:00:00Z",
        "updated_at": "2026-02-22T10:00:00Z"
    }
    ```
-   **Status 401 Unauthorized**: If JWT is missing or invalid.
-   **Status 403 Forbidden**: If `{user_id}` in path does not match authenticated user, or `task_id` does not belong to user.
-   **Status 404 Not Found**: If the `task_id` does not exist for the authenticated user.
-   **Status 500 Internal Server Error**: For unexpected server issues.

---

### 3. `POST /api/{user_id}/tasks` - Create a New Task for a User

**Description**: Creates a new task for the authenticated user.
**Authentication**: Required (JWT)
**Authorization**: User must be authenticated and the `{user_id}` in the path must match the authenticated user's ID.
**Request**:
-   **Method**: `POST`
-   **Headers**:
    -   `Authorization: Bearer <JWT_TOKEN>`
    -   `Content-Type: application/json`
-   **Body**:
    ```json
    {
        "description": "New task description"
    }
    ```
    -   `description` (string, required): The description of the new task.
**Response**:
-   **Status 201 Created**:
    ```json
    {
        "id": "generated-uuid-of-new-task",
        "description": "New task description",
        "status": "Pending",
        "created_at": "2026-02-22T12:30:00Z",
        "updated_at": "2026-02-22T12:30:00Z"
    }
    ```
-   **Status 400 Bad Request**: If `description` is missing or empty.
-   **Status 401 Unauthorized**: If JWT is missing or invalid.
-   **Status 403 Forbidden**: If `{user_id}` in path does not match authenticated user.
-   **Status 500 Internal Server Error**: For unexpected server issues.

---

### 4. `PUT /api/{user_id}/tasks/{task_id}` - Fully Update a Specific Task for a User

**Description**: Replaces an existing task for the authenticated user with new data.
**Authentication**: Required (JWT)
**Authorization**: User must be authenticated and the `{user_id}` in the path must match the authenticated user's ID. The `task_id` must belong to the authenticated user.
**Request**:
-   **Method**: `PUT`
-   **Path Parameters**:
    -   `task_id` (UUID): The unique identifier of the task to update.
-   **Headers**:
    -   `Authorization: Bearer <JWT_TOKEN>`
    -   `Content-Type: application/json`
-   **Body**:
    ```json
    {
        "description": "Updated task description",
        "status": "Complete"
    }
    ```
    -   `description` (string, required): The new description for the task.
    -   `status` (string, required): The new status for the task ("Pending" or "Complete").
**Response**:
-   **Status 200 OK**:
    ```json
    {
        "id": "uuid-of-task",
        "description": "Updated task description",
        "status": "Complete",
        "created_at": "2026-02-22T10:00:00Z",
        "updated_at": "2026-02-22T13:00:00Z"
    }
    ```
-   **Status 400 Bad Request**: If `description` or `status` is missing, empty, or invalid.
-   **Status 401 Unauthorized**: If JWT is missing or invalid.
-   **Status 403 Forbidden**: If `{user_id}` in path does not match authenticated user, or `task_id` does not belong to user.
-   **Status 404 Not Found**: If the `task_id` does not exist for the authenticated user.
-   **Status 500 Internal Server Error**: For unexpected server issues.

---

### 5. `PATCH /api/{user_id}/tasks/{task_id}` - Partially Update a Specific Task for a User

**Description**: Partially updates an existing task for the authenticated user.
**Authentication**: Required (JWT)
**Authorization**: User must be authenticated and the `{user_id}` in the path must match the authenticated user's ID. The `task_id` must belong to the authenticated user.
**Request**:
-   **Method**: `PATCH`
-   **Path Parameters**:
    -   `task_id` (UUID): The unique identifier of the task to partially update.
-   **Headers**:
    -   `Authorization: Bearer <JWT_TOKEN>`
    -   `Content-Type: application/json`
-   **Body**:
    ```json
    {
        "description": "New partial description"
    }
    ```
    OR
    ```json
    {
        "status": "Complete"
    }
    ```
    -   `description` (string, optional): The new description for the task.
    -   `status` (string, optional): The new status for the task ("Pending" or "Complete").
**Response**:
-   **Status 200 OK**:
    ```json
    {
        "id": "uuid-of-task",
        "description": "New partial description",
        "status": "Pending",
        "created_at": "2026-02-22T10:00:00Z",
        "updated_at": "2026-02-22T13:30:00Z"
    }
    ```
-   **Status 400 Bad Request**: If provided `status` is invalid.
-   **Status 401 Unauthorized**: If JWT is missing or invalid.
-   **Status 403 Forbidden**: If `{user_id}` in path does not match authenticated user, or `task_id` does not belong to user.
-   **Status 404 Not Found**: If the `task_id` does not exist for the authenticated user.
-   **Status 500 Internal Server Error**: For unexpected server issues.

---

### 6. `DELETE /api/{user_id}/tasks/{task_id}` - Delete a Specific Task for a User

**Description**: Deletes a specific task belonging to the authenticated user.
**Authentication**: Required (JWT)
**Authorization**: User must be authenticated and the `{user_id}` in the path must match the authenticated user's ID. The `task_id` must belong to the authenticated user.
**Request**:
-   **Method**: `DELETE`
-   **Path Parameters**:
    -   `task_id` (UUID): The unique identifier of the task to delete.
-   **Headers**:
    -   `Authorization: Bearer <JWT_TOKEN>`
**Response**:
-   **Status 204 No Content**: If the task was successfully deleted.
-   **Status 401 Unauthorized**: If JWT is missing or invalid.
-   **Status 403 Forbidden**: If `{user_id}` in path does not match authenticated user, or `task_id` does not belong to user.
-   **Status 404 Not Found**: If the `task_id` does not exist for the authenticated user.
-   **Status 500 Internal Server Error**: For unexpected server issues.
