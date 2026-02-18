from dotenv import load_dotenv
import os
import re


def security_check(api_key: str | None) -> str:

    if not api_key:
        return "[WARNING] No API key detected"

    for to_check in [
        "../ex0/construct.py",
        "../ex1/loading.py",
        "../ex1/requirements.txt",
        "../ex1/pyproject.toml"
    ]:

        try:

            with open(to_check) as git_file:
                if api_key in git_file.readlines():
                    return (
                        "[WARNING] API key has been detected "
                        f"in git repository ('{to_check}')"
                    )

        except OSError as oserr:
            print(f"Caught {oserr.__class__.__name__}: {oserr}\n")

    return "[OK] No hardcoded secrets detected"


def check_dotenv_config() -> str:

    try:

        with open(".env") as dotenv:

            for line in dotenv:
                if not re.match(r"[A-Z_]+=", line):
                    return (
                        "[WARNING] .env file not properly configured "
                        f"- Check format for line: {line}"
                    )

    except OSError as oserr:
        return f"[ERROR] {oserr}"

    return "[OK] .env file properly configured"


def load_configuration(variables: dict[str, str | None]) -> None:

    defaults: dict[str, str] = {
        "MATRIX_MODE": "No mode selected",
        "DATABASE_URL": "Not connected to a database",
        "API_KEY": "Not authenticated",
        "LOG_LEVEL": "NONE",
        "ZION_ENDPOINT": "Offline"
    }

    print("Configuration loaded:\n")

    print(
        "Mode: "
        + (
            variables["MATRIX_MODE"]
            if variables["MATRIX_MODE"]
            else defaults["MATRIX_MODE"]
        )
    )
    print(
        "Database: "
        + (
            "Connected to local instance"
            if variables["DATABASE_URL"]
            else defaults["DATABASE_URL"]
        )
    )
    print(
        "API Access: "
        + (
            "Authenticated"
            if variables["API_KEY"]
            else defaults["API_KEY"]
        )
    )
    print(
        "Log Level: "
        + (
            variables["LOG_LEVEL"]
            if variables["LOG_LEVEL"]
            else defaults["LOG_LEVEL"]
        )
    )
    print(
        "Zion Network: "
        + (
            "Online"
            if variables["ZION_ENDPOINT"]
            else defaults["ZION_ENDPOINT"]
        )
    )


def main() -> None:

    print("\nORACLE STATUS: Reading the Matrix...\n")

    variables: dict[str, str | None] = {
        var_name: None
        for var_name in [
            "MATRIX_MODE",
            "DATABASE_URL",
            "API_KEY",
            "LOG_LEVEL",
            "ZION_ENDPOINT"
        ]
    }

    fst: bool = True

    for _ in range(2):

        to_load: list[str] = [
            var_name for var_name, var in variables.items() if not var
        ]

        if not fst:

            overrided: list[str] = [
                var_name for var_name, var in variables.items() if var
            ]
            load_dotenv()

        for env in to_load:
            variables[env] = os.getenv(env)

        fst = False

    missing_variables: list[str] = [
        var_name for var_name, var, in variables.items() if not var
    ]

    if missing_variables:

        print("Missing configuration variables:\n")

        for var in missing_variables:
            print(f"[MISSING] {var}")

        print(
            "\nPlease add the missing environment variables "
            "to properly load configuration\n"
        )

    load_configuration(variables)

    print("\nEnvironment security check:\n")

    print(security_check(variables["API_KEY"]))

    print(check_dotenv_config())

    if overrided:

        print("[OK] Environment variables (", end="")

        fst = True

        for over in overrided:

            if not fst:
                print(", ", end="")

            print(over, end="")

            fst = False

        print(") overrided")

    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
