import os
from dhooks import Webhook, Embed, File

image2_path = 'cs-aor1-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[CS link - click here -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/view.php?id=10239)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://cs-aor1-nova-obavestenja.png")
    file = File(image2_path, name="cs-aor1-nova-obavestenja.png")
    hook.send("@everyone 📢 AOR-1", embed=embed, file=file)
