from crontab import CronTab
from service.EmailService import EmailService;
import os;
from EmailScan import startEmailScan
import time
def main():
    #object declaration and function call;
    print("program start ");
    # script_path = './EmailScan.py'  # Adjust this path
    # if not os.path.exists(script_path):
    #     raise FileNotFoundError(f"Script not found: {script_path}")
    # else:
    #     print("all good...")
    
    # python_interpreter = 'C:/Users/saroj/AppData/Local/Programs/Python/Python312/python.exe'  # Adjust this path if needed
    # if not os.path.exists(python_interpreter):
    #     raise FileNotFoundError(f"Python interpreter not found: {python_interpreter}")
    # else:
    #     print("all good...")
    # cron_command = f'{python_interpreter} {script_path}'

    # cron = CronTab(user='saroj')
    # command = f'{python_interpreter} {script_path}'
    # job = cron.new(command=command)
    # job.minute.every(1)

    # # Write the job to the crontab
    # cron.write()
        
    # # with CronTab(user=r'atharv\saroj') as cron:
    # #     print("cron started...")
    # #     job = cron.new(command=cron_command)
    # #     job.minute.every(1);
# def startEmailScan():
#     emailService = EmailService();
#     client = emailService.getReadEmailClient();
#     messages = emailService.fetchEmail(client);
#     for msg in messages:
#         # Print form and subject
#         print(msg.from_, ': ', msg.subject);
#         # Print the plain text (if there is one)
#         print(msg.text);
#         print("UID :"+msg.uid);
#         print(msg);
while(1):
    startEmailScan();
    time.sleep(30);



if __name__ == "__main__":
    main()