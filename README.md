# Module-3

A simple Python script demonstrating the use of **decorators** for logging and role-based access control (admin authorization) in an Employee Management context.

## Overview

This project shows how Python decorators can be combined to add cross-cutting functionality — logging and authentication — to business logic functions without modifying their core code.

It implements two decorators:

- **`@logger`** – Logs every function call (to both console and a log file) whenever a decorated function is executed.
- **`@admin_required`** – Restricts execution of a function to users with the `admin` role. If the current user is not an admin, access is denied and a warning is logged.

These decorators are applied to three sample employee management functions:

- `add_employee()`
- `update_employee()`
- `delete_employee()`

## Project Structure

```
Module-3/
├── main.py              # Main script with decorators and employee functions
└── logs/
    └── application.log  # Auto-generated log file (created at runtime)
```

## How It Works

1. On startup, a `logs/` folder is created (if it doesn't already exist) to store log output.
2. Logging is configured to write timestamped INFO/WARNING messages to `logs/application.log`.
3. A `current_user` dictionary simulates the logged-in user, with a `name` and `role`.
4. Each employee function is decorated with `@logger` and `@admin_required`:
   - `@admin_required` checks if `current_user["role"] == "admin"`. If true, the function runs; otherwise, access is denied and a warning is logged.
   - `@logger` logs and prints the name of the function being executed.

## Requirements

- Python 3.x (no external dependencies — uses only the standard library)

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/riteshkodshetti3112/Module-3.git
cd Module-3
python main.py
```

### Expected Output (when `role` is `"admin"`)

```
[LOG] add_employee executed
Employee Added Successfully
[LOG] update_employee executed
Employee Updated Successfully
[LOG] delete_employee executed
Employee Deleted Successfully
```

### Testing Access Control

To test the authorization check, open `main.py` and change the role in `current_user`:

```python
current_user = {
    "name": "Ritesh",
    "role": "user"   # change to "user" to test
}
```

Re-running the script will now deny access to all employee operations and log warnings instead:

```
[ACCESS DENIED] Admin only operation
[ACCESS DENIED] Admin only operation
[ACCESS DENIED] Admin only operation
```

## Logging

All function executions and unauthorized access attempts are recorded in `logs/application.log` with timestamps, log level, and message — useful for auditing and debugging.

Example log entries:

```
2026-06-30 10:00:00 - INFO - add_employee function executed
2026-06-30 10:00:05 - WARNING - Unauthorized access attempt: delete_employee
```

## Author

**Ritesh Kodshetti**
