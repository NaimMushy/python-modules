def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files: list[str] = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    messages: dict[str, str | dict[str, str]] = {
        "access_msg": "Attempting access to",
        "FileNotFoundError": {
            "resp": "[RESPONSE] Archive not found in storage matrix",
            "status": "[STATUS] Crisis handled - System stable\n"
        },
        "PermissionError": {
            "resp": "[RESPONSE] Security protocols deny access",
            "status": "[STATUS] Crisis handled - Security maintained\n"
        },
        "success_msg": "[SUCCESS] Archive recovered - ",
        "success_status": "[STATUS] Normal operations resumed\n"
    }

    for filename in files:

        try:
            with open(filename) as file:
                print(
                    f"[ROUTINE ACCESS] {messages['access_msg']} "
                    f"'{filename}'..."
                )
                print(f"{messages['success_msg']}'{file.read()}'")
                print(messages["success_status"])

        except (FileNotFoundError, PermissionError) as err:
            print(f"[CRISIS ALERT] {messages['access_msg']} '{filename}'...")
            print(messages[err.__class__.__name__]["resp"])
            print(messages[err.__class__.__name__]["status"])

    print("All crisis scenarios handled successfully - Archive secure")


if __name__ == "__main__":
    main()
