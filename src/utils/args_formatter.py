import argparse


class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        if type(action) is argparse._SubParsersAction:
            parts = []
            for subaction in action._get_subactions():
                parts.append(f"  {subaction.metavar:<18}{subaction.help}")
            return "\n".join(parts) + "\n"
        return super()._format_action(action)
