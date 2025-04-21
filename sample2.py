# The math module was imported so that the program works
import math

multiChannel = 0

def ChannelSubract(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue -= value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)
    

def ChannelAdd(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue += value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)

def ChannelSetValue(channelID, value):
    global multiChannel
    if not ValidateValue(value): return
    ChannelClear(channelID)
    value = value * (1000**(channelID - 1))
    multiChannel += value

def ChannelClear(channelID):
    global multiChannel
    if channelID == -1:
        multiChannel = 0
    else:
        channel_value = ChannelGetValue(channelID) * (1000 ** (channelID - 1))
        multiChannel -= channel_value

def ValidateValue(value):
    if value < 999 and value > 0: 
        return True
    else:
        print("Value out of range, operation not performed") 
        return False

def DisplayAllChannels():
    value = ChannelGetValue(1)
    print(f"Channel 1 is {value}")
    value = ChannelGetValue(2)
    print(f"Channel 2 is {value}")
    value = ChannelGetValue(3)
    print(f"Channel 3 is {value}")

def ChannelGetValue(channelID):
    result = math.floor(multiChannel % (1000**channelID) / (1000**(channelID - 1)))
    return result


###DO NOT ALTER ANY CODE BELOW THIS LINE###

def main():    
    global multiChannel
    multiChannel = 123456789
    ChannelSetValue(2,555)
    ChannelSubract(2,111)
    DisplayAllChannels()
    ChannelClear(-1)
    ChannelSubract(3,1)
    ChannelSetValue(1,111)
    ChannelSetValue(2,888)
    DisplayAllChannels()
    ChannelSubract(1,111)
    ChannelAdd(2,111)
    ChannelAdd(3,5555)
    DisplayAllChannels()





#Start the program
if __name__ == "__main__":
    main()

print("Program terminated")
