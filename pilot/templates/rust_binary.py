def install_hook(_):
    """
    Command to run to complete the project scaffolding setup.

    :param project: the project object
    """


RUST_BINARY = {
    "path": "rust_binary",
    "description": "Rust application with a binary executable",
    "summary": "\n".join(
        [
            "* initial Rust binary setup",
            "* binary description is in `Cargo.toml`",
            "* entrypoint is `src/main.rs`",
        ]
    ),
    "install_hook": install_hook,
    "files": {
        "Cargo.toml": "This file is used to define the metadata and dependencies for the Rust project. It specifies the project name, version, authors, edition, and dependencies required by the project.",
        "src/main.rs": "This file represents the entry point for the Rust application. It contains the main function that serves as the starting point for the program execution. You can define the application logic and functionality in this file.",
    },
}
