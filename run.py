from highrise.__main__ import BotDefinition, main, import_module, arun
import time

room_id = "6262f2ece62063a56f1375c9"
bot_token = "721fbe70a38729a2a52d360799c3f44fd51726f11b665848c0245bdecce73d41"
bot_file = "main"
bot_class = "MyBot"

if __name__ == "__main__":
  definitions = [
    BotDefinition(
      getattr(import_module(bot_file), bot_class)(),
      room_id, 
      bot_token)]  # More BotDefinition classes can be added to the definitions list
  while True:
    try:
      arun(main(definitions))
    except Exception as e:
      # Print the full traceback for the exception
      import traceback
      print("Caught an exception:")
      traceback.print_exc()  # This will print the full traceback       
      time.sleep(10)       
      continue
