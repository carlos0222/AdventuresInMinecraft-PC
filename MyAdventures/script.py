# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep, time

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

start_time = time()

while True:
    pos = mc.player.getTilePos()
    if(mc.getBlock(pos.x, pos.y-1, pos.z) != block.GOLD_BLOCK.id and mc.getBlock(pos.x, pos.y-1, pos.z) != block.AIR.id):
        mc.setBlock(pos.x, pos.y-1, pos.z, block.GOLD_BLOCK.id)

    if time() - start_time > 10:
        mc.postToChat("ALGO CADA CIERTO TIEMPO")
        start_time = time()

    sleep(0.1)