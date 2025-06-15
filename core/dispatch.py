from modules.dropperlab.dropper import run_dropper
from modules.stage1.stage1 import run_stage1
from modules.stage2.stage2 import run_stage2
from modules.endgame.endgame import run_endgame
from modules.payloadlab.payload import payload_menu
from modules.telemetry.telemetry import telemetry_menu
from modules.crypter.crypter import crypter_menu
from modules.guard.guard import guard_menu
from modules.vault.vault import vault_menu
from modules.sharedspace.session import session_menu
from modules.dashboard.dashboard import dashboard_menu

def dispatch_command(cmd):
    commands = {
        "dropperlab": run_dropper,
        "stage1": run_stage1,
        "stage2": run_stage2,
        "endgame": run_endgame,
        "payloadlab": payload_menu,
        "telemetry": telemetry_menu,
        "crypter": crypter_menu,
        "guard": guard_menu,
        "vault": vault_menu,
        "sharedspace": session_menu,
        "dashboard": dashboard_menu
    }
    if cmd in commands:
        commands[cmd]()
    else:
        print(f"[!] Unknown command: {cmd}")
