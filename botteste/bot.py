"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Teste de automação do chart
        self.execute(r'C:\Users\u129510\Downloads\CLEARCHART_TESTE (1).exe')
        if not self.find( "login", matching=0.97, waiting_time=10000):
            self.not_found("login")
        self.click()
        
        if not self.find( "data", matching=0.97, waiting_time=10000):
            self.not_found("data")
        self.click()
        self.paste('30/09/2022')
        
        if not self.find( "hora_inicial", matching=0.97, waiting_time=10000):
            self.not_found("hora_inicial")
        self.click()
        self.paste('11:00')
        
        if not self.find( "hora_final", matching=0.97, waiting_time=10000):
            self.not_found("hora_final")
        self.click()
        self.paste('16:00')
        
        
        if not self.find( "PCA", matching=0.97, waiting_time=10000):
            self.not_found("PCA")
        self.click()
        self.paste('Andre Aliot')
        
        if not self.find( "nome", matching=0.97, waiting_time=10000):
            self.not_found("nome")
        self.click()
        
        self.paste('teste')
        
        if not self.find( "SAP", matching=0.97, waiting_time=10000):
            self.not_found("SAP")
        self.click()
        self.paste('0000')
        
        
        if not self.find( "evento", matching=0.97, waiting_time=10000):
            self.not_found("evento")
        self.click()
        
        self.paste('Submissão de caso')
        
        if not self.find( "caso", matching=0.97, waiting_time=10000):
            self.not_found("caso")
        self.click()
        
        self.paste('teste')
        
        if not self.find( "setup", matching=0.97, waiting_time=10000):
            self.not_found("setup")
        self.click()
        
        if not self.find( "encaminhar", matching=0.97, waiting_time=10000):
            self.not_found("encaminhar")
        self.click()


        if not self.find( "AdiconarAoSQL", matching=0.97, waiting_time=10000):
            self.not_found("AdiconarAoSQL")
        self.click()

        


        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()











