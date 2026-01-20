ACCESS_MSG: str = "attempting access to"
FILENOTFOUNDERR_RES: str = "[response] archive not found in storage matrix"
FILENOTFOUNDERR_STATUS: str = "[status] crisis handled - system stable\n"
PERMISSIONERR_RES: str = "[response] security protocols deny access"
PERMISSIONERR_STATUS: str = "[status] crisis handled - security maintained\n"
SUCCESS_MSG: str = "[success] archive recovered - "
SUCCESS_STATUS: str = "[status] normal operations resumed\n"


def main() -> None:
    """
    Attemps secure access to different archives, and handles errors properly.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files: list[str] = (
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    )
    for filename in files:
        try:
            with open(filename) as file:
                print(f"[routine access] {ACCESS_MSG} '{filename}'...")
                print(f"{SUCCESS_MSG}'{file.read()}'")
                print(SUCCESS_STATUS)
        except FileNotFoundError:
            print(f"[crisis alert] {ACCESS_MSG} '{filename}'...")
            print(FILENOTFOUNDERR_RES)
            print(FILENOTFOUNDERR_STATUS)
        except PermissionError:
            print(f"[crisis alert] {ACCESS_MSG} '{filename}'...")
            print(PERMISSIONERR_RES)
            print(PERMISSIONERR_STATUS)
    print("all crisis scenarios handled successfully - archive secure")


if __name__ == "__main__":
    main()
