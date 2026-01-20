def main() -> None:
    """
    Reads from and writes to files using the with statement for security.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("initializing secure vault access...")
    print("vault connection established with failsafe protocols\n")
    with open("classified_data.txt") as classified:
        print("---- secure extraction ----")
        for line in classified:
            print(line)
    print("\n")
    with open("security_protocols.txt", "a") as secure:
        print("---- secure preservation ----")
        secure.write("vault automatically sealed upon completion")
    with open("security_protocols.txt") as new_secure:
        for line in new_secure:
            print(line)
    print("\nall vault operations completed with maximum security")


if __name__ == "__main__":
    main()
