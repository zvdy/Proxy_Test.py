import subprocess


def main():
    print(""" 
    ____                           __            __                
   / __ \_________  _  ____  __   / /____  _____/ /_   ____  __  __
  / /_/ / ___/ __ \| |/_/ / / /  / __/ _ \/ ___/ __/  / __ \/ / / /
 / ____/ /  / /_/ />  </ /_/ /  / /_/  __(__  ) /_   / /_/ / /_/ / 
/_/   /_/   \____/_/|_|\__, /   \__/\___/____/\__/  / .___/\__, /  
                      /____/                       /_/    /____/   

    """)

    # Get the URL asking for from the command line
    url = input("Enter the URL you want to test: ")
    # Get the number of times to run the script from the command line
    times = int(input("Enter the number of times you want to run the script: "))
    # Run the script the number of times specified
    for i in range(times):
        # Run curl to get the status code
        curl = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url], stdout=subprocess.PIPE)
        # Print the status code
        print(curl.stdout.decode("utf-8"))

    print("\nDone")
    
if __name__ == "__main__":
    main()




