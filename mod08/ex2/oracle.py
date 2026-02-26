from dotenv import load_dotenv
import os
import re


def security_check(api_key: str | None) -> str:

    """ Checks whether or not there is a security leak for the API key """

    if not api_key:
        return "[WARNING] No API key detected"

    # searching in every file in the git repository

    for to_check in [
        "../ex0/construct.py",
        "../ex1/loading.py",
        "../ex1/requirements.txt",
        "../ex1/pyproject.toml"
    ]:

        # verifies if the API key appears in the file

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

    """ Checks if the .env file format corresponds to what is expected """

    try:

        with open(".env") as dotenv:

            # verifies the formatting of each line in the .env

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

    """
    Loads the matrix configuration
    based on the environment variables recovered
    """

    # setting default values for environment variables if not set

    defaults: dict[str, str] = {
        "MATRIX_MODE": "No mode selected",
        "DATABASE_URL": "Not connected to a database",
        "API_KEY": "Not authenticated",
        "LOG_LEVEL": "NONE",
        "ZION_ENDPOINT": "Offline"
    }

    print("Configuration loaded:\n")

    # displaying the loaded configuration information

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

    """
    Recovers the environment variables
    Loads configuration
    Completes validation through security and formatting checks
    """

    print("\nORACLE STATUS: Reading the Matrix...\n")

    # initializing a dictionary to contain the environment variables

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

    # recovering environment variables
    # first checking for overrided variables from the command line
    # then loading the remaining from the .env file

    for loading in range(2):

        # establishing a list of environment variables to load
        # excluding those that are already recovered

        to_load: list[str] = [
            var_name for var_name, var in variables.items() if not var
        ]

        if loading > 0:

            # storing the environment variables
            # already recovered from the command line
            # in a list of overrided variables

            overrided: list[str] = [
                var_name for var_name, var in variables.items() if var
            ]

            # getting the remaining environment variables from the .env file

            load_dotenv()

        # storing the loaded environment variables in the variables dict

        for env in to_load:
            variables[env] = os.getenv(env)

    # setting a list of missing environment variables

    missing_variables: list[str] = [
        var_name for var_name, var, in variables.items() if not var
    ]

    if missing_variables:

        # displaying information about the missing variables

        print("Missing configuration variables:\n")

        for var in missing_variables:
            print(f"[MISSING] {var}")

        print(
            "\nPlease add the missing environment variables "
            "to properly load configuration\n"
        )

    # loading configuration and performing checks

    load_configuration(variables)

    print("\nEnvironment security check:\n")

    print(security_check(variables["API_KEY"]))

    print(check_dotenv_config())

    if overrided:

        # displaying information about the overrided environment variables

        print("[OK] Environment variables ({','.join(overrided)}) overrided")

    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
