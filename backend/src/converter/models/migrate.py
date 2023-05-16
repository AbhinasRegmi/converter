from converter.models.user_model import initialize as user_ini


if __name__ == "__main__":
    print("Starting migrations.....")

    user_ini()

    print("Migration completed.")



