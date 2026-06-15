import os
import logging
from functools import wraps

# =========================
# CREATE LOG FOLDER
# =========================
os.makedirs("logs", exist_ok=True)

# =========================
# LOGGING CONFIGURATION
# =========================
logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# SAMPLE USER (AUTH CHECK)
# =========================
current_user = {
    "name": "Ritesh",
    "role": "admin"   # change to "user" to test
}

# =========================
# LOGGER DECORATOR
# =========================
def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        logging.info(f"{func.__name__} function executed")

        print(f"[LOG] {func.__name__} executed")

        return func(*args, **kwargs)

    return wrapper


# =========================
# AUTH DECORATOR
# =========================
def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.get("role") == "admin":
            return func(*args, **kwargs)
        else:
            print("[ACCESS DENIED] Admin only operation")
            logging.warning(f"Unauthorized access attempt: {func.__name__}")

    return wrapper


# =========================
# EMPLOYEE FUNCTIONS
# =========================

@logger
@admin_required
def add_employee():
    print("Employee Added Successfully")


@logger
@admin_required
def update_employee():
    print("Employee Updated Successfully")


@logger
@admin_required
def delete_employee():
    print("Employee Deleted Successfully")


# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":

    add_employee()
    update_employee()
    delete_employee()