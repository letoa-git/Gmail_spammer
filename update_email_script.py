import re
import subprocess


def print_ascii_logo():
    dark_purple_text = '\033[38;5;55m'
    dark_bg = '\033[48;5;0m'
    reset = '\033[0m'
    logo = f"""
    {dark_bg}{dark_purple_text} 
                                   __  __                                                                                     
                                  |  \|  \                                                                                    
  ______   ______ ____    ______   \$$| $$        _______   ______    ______   ______ ____   ______ ____    ______    ______  
 /      \ |      \    \  |      \ |  \| $$       /       \ /      \  |      \ |      \    \ |      \    \  /      \  /      \ 
|  $$$$$$\| $$$$$$\$$$$\  \$$$$$$\| $$| $$      |  $$$$$$$|  $$$$$$\  \$$$$$$\| $$$$$$\$$$$\| $$$$$$\$$$$\|  $$$$$$\|  $$$$$$
| $$  | $$| $$ | $$ | $$ /      $$| $$| $$       \$$    \ | $$  | $$ /      $$| $$ | $$ | $$| $$ | $$ | $$| $$    $$| $$   \$$
| $$__| $$| $$ | $$ | $$|  $$$$$$$| $$| $$       _\$$$$$$\| $$__/ $$|  $$$$$$$| $$ | $$ | $$| $$ | $$ | $$| $$$$$$$$| $$      
 \$$    $$| $$ | $$ | $$ \$$    $$| $$| $$      |       $$| $$    $$ \$$    $$| $$ | $$ | $$| $$ | $$ | $$ \$$     \| $$      
 _\$$$$$$$ \$$  \$$  \$$  \$$$$$$$ \$$ \$$       \$$$$$$$ | $$$$$$$   \$$$$$$$ \$$  \$$  \$$ \$$  \$$  \$$  \$$$$$$$ \$$      
|  \__| $$                                                | $$                                                                
 \$$    $$                                                | $$                                                                
  \$$$$$$                                                  \$$                                                                
__________________________________________________________________________________________________________________________________
                                                    by : letoa-git x MaciSlam
                                                                                                                                
----------------------------------------------------------------------------------------------------------------------------------
     
 {reset}
    """
    print(logo)


def get_user_input():
    target_email = input("Enter target's Gmail: ")
    your_email = input("Enter your Gmail: ")
    your_password = input("Enter your Gmail key password: ")
    message = input("Enter the message to send: ")
    return target_email, your_email, your_password, message


def update_original_script(target_email, your_email, your_password, message):
    try:
        with open('original_script.py', 'r') as file:
            content = file.read()

        # Update the variables in the original script
        content = re.sub(r"toaddrs = '.*?'", f"toaddrs = '{target_email}'", content)
        content = re.sub(r"fromaddrs = '.*?'", f"fromaddrs = '{your_email}'", content)
        content = re.sub(r"message = '.*?'", f"message = '{message}'", content)
        content = re.sub(r"smtpserver.login\('.*?', '.*?'\)", f"smtpserver.login('{your_email}', '{your_password}')",
                         content)

        with open('original_script.py', 'w') as file:
            file.write(content)
        print("Original script has been updated with the new values.")
    except Exception as e:
        print(f"Error updating original_script.py: {e}")


def run_original_script():
    try:
        # Run the updated original_script.py
        print("Starting the spam process...")
        subprocess.run(["python", "original_script.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running original_script.py: {e}")
    except FileNotFoundError:
        print("Error: original_script.py not found. Ensure it is in the same directory.")


if __name__ == "__main__":
    print_ascii_logo()  # Print the ASCII logo when the script starts
    target_email, your_email, your_password, message = get_user_input()
    update_original_script(target_email, your_email, your_password, message)
    run_original_script()

