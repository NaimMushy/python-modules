def secure_access(filename: str) -> None:
    print("Initializing secure vault access...")

    try:
        with open(filename) as classified:
            print("Vault connection established with failsafe protocols")

            print("\n---- SECURE EXTRACTION ----")
            print(classified.read())

        with open(filename, "w") as classified:
            print("\n---- SECURE PRESERVATION ----")
            with open("security_protocols.txt") as security_protocols:
                for line in security_protocols:
                    print(line)
                    classified.write(line)

    except (FileNotFoundError, PermissionError) as ve:
        print(f"ERROR: {ve}")

    finally:
        print("Vault automatically sealed upon completion")


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    secure_access("classified_data.txt")

    print("\nAll vault operations completed with maximum security")


if __name__ == "__main__":
    main()
