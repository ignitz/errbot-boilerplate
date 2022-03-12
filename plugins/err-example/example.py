from errbot import BotPlugin, botcmd, re_botcmd
import re


class Example(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """

        return "Try me bitch!"  # This string format is markdown.

    @re_botcmd(pattern=r"^test a message$", template="test_message", prefixed=False)
    def test_message(self, msg, args):  # a command callable with !tryme
        print(msg)
        print(msg._from)
        return {"name": "MeuLindo"}

    @re_botcmd(pattern=r"(^| )cookies?( |$)", prefixed=False, flags=re.IGNORECASE)
    def listen_for_talk_of_cookies(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "Somebody mentioned cookies? Om nom nom!"
