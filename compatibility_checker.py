import hashlib
import tkinter as tk
from tkinter import font, messagebox
import webbrowser

WINDOW_TITLE = "Name Compatibility Checker"
WINDOW_SIZE = "420x340"
GITHUB_URL = "https://github.com/LofiDev47"


def normalize_name(raw_name: str) -> str:
    """Normalize and title-case a user-provided name."""
    return raw_name.strip().title()


def is_valid_name(name: str) -> bool:
    """Return True when a name is non-empty and contains alphabetic characters only."""
    return bool(name) and name.isalpha()


def compatibility_score(name1: str, name2: str) -> int:
    """Compute a deterministic compatibility score from 0 to 100 for two names."""
    ordered_names = "|".join(sorted((name1, name2))).encode("utf-8")
    digest = hashlib.sha256(ordered_names).hexdigest()
    return int(digest[:8], 16) % 101


def open_github() -> None:
    webbrowser.open_new(GITHUB_URL)


def build_ui() -> tk.Tk:
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.resizable(False, False)

    custom_font = font.Font(family="Segoe UI", size=11)
    header_font = font.Font(family="Segoe UI", size=15, weight="bold")

    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(expand=True, fill="both")

    header = tk.Label(
        main_frame,
        text="💖 Name Compatibility Checker 💖",
        font=header_font,
        fg="#d6336c",
        wraplength=400,
        justify="center",
    )
    header.grid(row=0, column=0, pady=(10, 15), sticky="ew")

    tk.Label(main_frame, text="Enter the first name:", font=custom_font).grid(
        row=1, column=0, sticky="w", pady=(0, 5)
    )
    entry_name1 = tk.Entry(main_frame, font=custom_font)
    entry_name1.grid(row=2, column=0, sticky="ew", pady=(0, 10))

    tk.Label(main_frame, text="Enter the second name:", font=custom_font).grid(
        row=3, column=0, sticky="w", pady=(0, 5)
    )
    entry_name2 = tk.Entry(main_frame, font=custom_font)
    entry_name2.grid(row=4, column=0, sticky="ew", pady=(0, 10))

    result_label = tk.Label(
        main_frame,
        text="",
        font=custom_font,
        fg="#333366",
        wraplength=320,
        justify="center",
    )
    result_label.grid(row=6, column=0, pady=(10, 20))

    def check_compatibility(event=None) -> None:
        del event
        name1 = normalize_name(entry_name1.get())
        name2 = normalize_name(entry_name2.get())

        if not is_valid_name(name1) or not is_valid_name(name2):
            messagebox.showerror(
                "Invalid Input", "Please enter valid names (letters only)."
            )
            return

        score = compatibility_score(name1, name2)
        result_label.config(
            text=f"The compatibility score for {name1} and {name2} is {score}%!"
        )

        entry_name1.delete(0, tk.END)
        entry_name2.delete(0, tk.END)
        entry_name1.focus()

    check_btn = tk.Button(
        main_frame,
        text="Check Compatibility",
        font=custom_font,
        bg="#4CAF50",
        fg="white",
        command=check_compatibility,
    )
    check_btn.grid(row=5, column=0, pady=(0, 10), sticky="ew")

    github_link = tk.Label(
        main_frame,
        text="My GitHub",
        font=custom_font,
        fg="#1a0dab",
        cursor="hand2",
    )
    github_link.grid(row=7, column=0, pady=(0, 10))
    github_link.bind("<Button-1>", lambda _: open_github())

    exit_btn = tk.Button(
        main_frame,
        text="Exit",
        font=custom_font,
        bg="#d9534f",
        fg="white",
        command=root.destroy,
    )
    exit_btn.grid(row=8, column=0, pady=(0, 10), sticky="ew")

    main_frame.columnconfigure(0, weight=1)

    root.bind("<Return>", check_compatibility)
    entry_name1.focus()

    return root


def main() -> None:
    app = build_ui()
    app.mainloop()


if __name__ == "__main__":
    main()
