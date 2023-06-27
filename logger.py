from datetime import datetime 


def write_to_history(success: bool, user: str, message: str, channel):
    dt = datetime.now()
    t = dt.time()
    d = dt.date()

    dest: str = f"./logs/{d}.log" 
    interaction: str = f"{success}, {t}, {user}, {message}, {channel}"

    with open(dest, mode="a+", encoding="utf-8") as history:
        history.write(f"{interaction}\n")

    
    



