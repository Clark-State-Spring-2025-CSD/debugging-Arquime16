# The math module was imported so that the program works.
import math

#The variable was set to be used in the block of code.
multiChannel = 0

# A function was made to subtract the arguments, parameters and reach the aim of the problem.
def ChannelSubract(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue -= value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)
    
# A function was made to add value, variables, parameters, arguments and to reach the aim of the problem.
def ChannelAdd(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue += value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)

# A function was made to set the operation and calculate the values.
def ChannelSetValue(channelID, value):
    global multiChannel
    if not ValidateValue(value): return
    ChannelClear(channelID)
    value = value * (1000**(channelID - 1))
    multiChannel += value

# A function was made to clear and obtain the values that want to reach in the operation.
def ChannelClear(channelID):
    global multiChannel
    if channelID == -1:
        multiChannel = 0
    else:
        channel_value = ChannelGetValue(channelID) * (1000 ** (channelID - 1))
        multiChannel -= channel_value

# A function was made for validate the values and to set the range with numbers boolean. 
def ValidateValue(value):
    if value <= 999 and value >= 0: 
        return True
    else:
        print("Value out of range, operation not performed") 
        return False

# A function was made for to display all channels and get values requested.
def DisplayAllChannels():
    value = ChannelGetValue(1)
    print(f"Channel 1 is {value}")
    value = ChannelGetValue(2)
    print(f"Channel 2 is {value}")
    value = ChannelGetValue(3)
    print(f"Channel 3 is {value}")

# A function was made for to get the result math of the channels.
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
