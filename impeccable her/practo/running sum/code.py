#running sum of series at all indices


def runningbitch(ola):
    uber = []
    uber.append(ola[0])

    for i in range(1, len(ola)):
        uber.append(ola[i]+uber[i-1])

    return uber

def realbitch(uber, i , j ):
    if i == 0:
        return uber[j]
    return (uber[j]-uber[i-1])


if __name__ == "__main__":

    ola = [1,2,3,4,5,6,7,8]
    rs = runningbitch(ola)
    print(rs)

    faketaxi = realbitch(rs, 1,3)

    print(faketaxi)



    #thats how you write a perfect vulgar code
    #bow and learn

    