import subprocess

result = subprocess.run(
    "echo Hello World",  # pass the full command as a single string
    shell=True,          # must be True on Windows for shell commands
    capture_output=True,
    text=True
)

print(result.stdout)
