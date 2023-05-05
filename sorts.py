'''
SORTING ALGORITHM VISUALISER
Notes:
    The reset button does not work for the following sorts:
        Quick
        Merge
        Stooge
        Shell

    I was planning to add sound effects but getting that to work using python was difficult.

'''



import random, math, pygame as pg

pg.init()


class DrawInformation:
    black = 0, 0, 0
    white = 255, 255, 255
    green = 242, 19, 242
    red = 255, 0, 0
    backgroundColour = white
    sidePad = 20
    topPad = 150
    font = pg.font.SysFont('consolas', 20)
    colours = [(55, 187, 203), (57, 180, 146), (42, 102, 150), (110, 148, 187)]

    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption("Sorting Algorithm Visualiser")
        self.setList(list)

    def setList(self, list):
        self.list = list
        self.maxValue = max(list)
        self.minValue = min(list)
        self.columnWidth = (self.width - self.sidePad) // len(list)
        self.columnHeight = math.floor((self.height - self.topPad) / (self.maxValue - self.minValue))
        self.startX = self.sidePad // 2


def generateList(n, mini, maxi):
    return [random.randint(mini, maxi) for _ in range(n)]


def draw(drawInfo, algoID):
    drawInfo.window.fill(drawInfo.backgroundColour)
    ID = drawInfo.font.render(f"Current Algorithm: {algoID}", 1, drawInfo.black)
    drawInfo.window.blit(ID, (drawInfo.width // 2 - ID.get_width() / 2, 5))
    drawInfo.window.blit(drawInfo.font.render("R: Reset", 1, drawInfo.black), (drawInfo.width - 95, 10))
    drawInfo.window.blit(drawInfo.font.render("SPACE: Start", 1, drawInfo.black), (drawInfo.width - 140, 30))
    controls = drawInfo.font.render(f"{len(drawInfo.list)} elements", 1, drawInfo.black)
    drawInfo.window.blit(controls, (drawInfo.width // 2 - controls.get_width() / 2, 30))
    drawInfo.window.blit(drawInfo.font.render("B: Bubble", 1, drawInfo.black), (10, 10))
    drawInfo.window.blit(drawInfo.font.render("I: Insertion", 1, drawInfo.black), (10, 30))
    drawInfo.window.blit(drawInfo.font.render("H: Heap", 1, drawInfo.black), (10, 50))
    drawInfo.window.blit(drawInfo.font.render("S: Selection", 1, drawInfo.black), (10, 70))
    drawInfo.window.blit(drawInfo.font.render("M: Merge", 1, drawInfo.black), (10, 90))
    drawInfo.window.blit(drawInfo.font.render("Q: Quick", 1, drawInfo.black), (10, 110))
    drawInfo.window.blit(drawInfo.font.render("X: Radix", 1, drawInfo.black), (10, 130))
    drawInfo.window.blit(drawInfo.font.render("O: Stooge", 1, drawInfo.black), (170, 10))
    drawInfo.window.blit(drawInfo.font.render("T: Shuttle", 1, drawInfo.black), (170, 30))
    drawInfo.window.blit(drawInfo.font.render("L: Shell", 1, drawInfo.black), (170, 50))
    drawInfo.window.blit(drawInfo.font.render("C: Comb", 1, drawInfo.black), (170, 70))
    drawInfo.window.blit(drawInfo.font.render("Y: Cycle", 1, drawInfo.black), (170, 90))
    drawInfo.window.blit(drawInfo.font.render("J: Tim", 1, drawInfo.black), (170, 110))
    drawList(drawInfo)
    pg.display.update()


def drawList(drawInfo, colourPositions=None, clearBG=False, arr=None):
    if colourPositions is None:
        colourPositions = {}
    if not arr:
        list = drawInfo.list
    else:
        list = arr
    if clearBG:
        clearRect = (drawInfo.sidePad // 2, drawInfo.topPad, drawInfo.width - drawInfo.sidePad, drawInfo.height)
        pg.draw.rect(drawInfo.window, drawInfo.backgroundColour, clearRect)
    for i, _ in enumerate(list):
        x = drawInfo.startX + i * drawInfo.columnWidth
        y = drawInfo.height - (_ - drawInfo.minValue) * drawInfo.columnHeight
        colour = drawInfo.colours[i % len(drawInfo.colours)]
        if i in colourPositions:
            colour = colourPositions[i]
        pg.draw.rect(drawInfo.window, colour, (x, y, drawInfo.columnWidth, drawInfo.height))
    if clearBG:
        pg.display.update()


def bubbleSort(drawInfo):
    list = drawInfo.list
    sorted = True
    while sorted == True:
        sorted = False
        for i in range(len(list)):
            for j in range(len(list) - i - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    drawList(drawInfo, {j: drawInfo.green, j + 1: drawInfo.red}, True)
                    yield True


def insertionSort(drawInfo):
    list = drawInfo.list
    for i in range(1, len(list)):
        current = list[i]
        while True:
            asc = i > 0 and list[i - 1] > current
            if not asc: break
            list[i] = list[i - 1]
            i -= 1
            list[i] = current
            drawList(drawInfo, {i - 1: drawInfo.green, i: drawInfo.red}, True)
            yield True


def heapSort(drawInfo, arr=False):
    if not arr: list = drawInfo.list
    for i in range(len(list) // 2 - 1, -1, -1):
        heapify(drawInfo, list, i, len(list))
        yield True
    for i in range(len(list) - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(drawInfo, list, 0, i)
        yield True


def heapify(drawInfo, list, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and list[left] > list[largest]:
        largest = left
    if right < n and list[right] > list[largest]:
        largest = right
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        drawList(drawInfo, {largest: drawInfo.green, i: drawInfo.red}, True)
        heapify(drawInfo, list, largest, n)


def selectionSort(drawInfo):
    list = drawInfo.list
    for i in range(len(list)):
        min = i
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
        drawList(drawInfo, {i: drawInfo.red, min: drawInfo.green}, True)
        yield True


def mergeSort(drawInfo):
    list = drawInfo.list
    merge1(list, 0, len(list) - 1, drawInfo)


def merge1(arr, l, r, drawInfo):
    if (l < r):
        m = l + (r - l) // 2
        merge1(arr, l, m, drawInfo)
        drawList(drawInfo, {l: drawInfo.green, m: drawInfo.red}, True)
        merge1(arr, m + 1, r, drawInfo)
        drawList(drawInfo, {m + 1: drawInfo.green, r: drawInfo.red}, True)
        merge(arr, l, m, r, drawInfo)


def merge(arr, start, mid, end, drawInfo):
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            while index != start:
                arr[index] = arr[index - 1]
                drawList(drawInfo, {index: drawInfo.green, index - 1: drawInfo.red}, True)
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1


def quickSort(drawInfo):
    quick(drawInfo)


def quick(drawInfo, start=0, end=None):
    arr = drawInfo.list
    if end is None:
        end = len(arr) - 1
    if end - start < 1:
        return
    pivot = random.randint(start, end)
    i = partition(drawInfo, start, end, pivot)
    quick(drawInfo, start, i - 1)
    quick(drawInfo, i + 1, end)


def partition(drawInfo, start, end, idx_pivot):
    array = drawInfo.list
    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = j = start + 1
    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            drawList(drawInfo, {i: drawInfo.green, j: drawInfo.red}, True)
            i += 1
        j += 1
    array[start], array[i - 1] = array[i - 1], array[start]
    drawList(drawInfo, {start: drawInfo.green, i - 1: drawInfo.red}, True)
    return i - 1


def radixSort(drawInfo):
    arr = drawInfo.list
    max1 = max(arr)
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp, drawInfo, 2)
        exp *= 2
        yield True


def countingSort(arr, exp1, drawInfo, base):
    n = len(arr)
    output = [0] * n
    count = [0] * base
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % base] += 1
    for i in range(1, base):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % base] - 1] = arr[i]
        drawList(drawInfo, {i: drawInfo.green, count[index % base] - 1: drawInfo.red}, True)
        count[index % base] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]


def stoogeSort(drawInfo):
    arr = drawInfo.list
    stooge(arr, drawInfo, 0, len(arr) - 1)


def stooge(arr, drawInfo, l, h):
    if l >= h:
        return
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
        drawList(drawInfo, {l: drawInfo.green, h: drawInfo.red}, True)
    if h - l + 1 > 2:
        a = int((h - l + 1) / 3)
        stooge(arr, drawInfo, l, h - a)
        stooge(arr, drawInfo, l + a, h)
        stooge(arr, drawInfo, l, h - a)


def shuttleSort(drawInfo):
    nums = drawInfo.list
    for i in range(len(nums) - 1, 0, -1):
        is_swapped = False
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                drawList(drawInfo, {j: drawInfo.green, j - 1: drawInfo.red}, True)
                is_swapped = True
                yield True
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                drawList(drawInfo, {j: drawInfo.green, j + 1: drawInfo.red}, True)
                is_swapped = True
                yield True
        if not is_swapped:
            return


def shellSort(drawInfo):
    array = drawInfo.list
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                drawList(drawInfo, {j: drawInfo.green, j - interval: drawInfo.red}, True)
                j -= interval
            array[j] = temp
        interval //= 2


def insertionSort(drawInfo, left=0, right=399):
    arr = drawInfo.list
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            drawList(drawInfo, {j: drawInfo.green, j - 1: drawInfo.red}, True)
            j -= 1
            yield True


def getNextGap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap


def combSort(drawInfo):
    arr = drawInfo.list
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                drawList(drawInfo, {i: drawInfo.green, i + gap: drawInfo.red}, True)
                swapped = True
                yield True


def cycleSort(drawInfo):
    array = drawInfo.list
    writes = 0
    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        writes += 1
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                if array[i] < item:
                    pos += 1
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            drawList(drawInfo, {pos: drawInfo.green, item: drawInfo.red}, True)
            yield True
            writes += 1


def insertion(arr, left, right, drawInfo):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            drawList(drawInfo, {j: drawInfo.green, j-1: drawInfo.red}, True)
            j -= 1


def calcMinRun(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def timSort(drawInfo):
    arr = drawInfo.list
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion(arr, start, end, drawInfo)
        yield True
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right, drawInfo)
                yield True
        size = 2 * size


def main():
    run, sorting = True, False
    # clock = pg.time.Clock()
    n, mini, maxi = 400, 5, 455
    drawInfo = DrawInformation(1250, 600, generateList(n, mini, maxi))
    sortAlgo = bubbleSort
    algoID = "Bubble"
    sortAlgoGen = None
    while run:
        # clock.tick(40)
        if sorting:
            try:
                next(sortAlgoGen)
            except:
                sorting = False
        else:
            draw(drawInfo, algoID)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type != pg.KEYDOWN:
                continue
            if event.key == pg.K_r:
                drawInfo.setList(generateList(n, mini, maxi))
                sorting = False
            elif event.key == pg.K_SPACE and not sorting:
                sorting = True
                sortAlgoGen = sortAlgo(drawInfo)
            elif event.key == pg.K_i and not sorting:
                sortAlgo = insertionSort
                algoID = "Insertion"
            elif event.key == pg.K_b and not sorting:
                sortAlgo = bubbleSort
                algoID = "Bubble"
            elif event.key == pg.K_h and not sorting:
                sortAlgo = heapSort
                algoID = "Heap"
            elif event.key == pg.K_s and not sorting:
                sortAlgo = selectionSort
                algoID = "Selection"
            elif event.key == pg.K_m and not sorting:
                sortAlgo = mergeSort
                algoID = "Merge"
            elif event.key == pg.K_q and not sorting:
                sortAlgo = quickSort
                algoID = "Quick"
            elif event.key == pg.K_x and not sorting:
                sortAlgo = radixSort
                algoID = "Radix"
            elif event.key == pg.K_o and not sorting:
                sortAlgo = stoogeSort
                algoID = "Stooge"
            elif event.key == pg.K_t and not sorting:
                sortAlgo = shuttleSort
                algoID = "Shuttle"
            elif event.key == pg.K_l and not sorting:
                sortAlgo = shellSort
                algoID = "Shell"
            elif event.key == pg.K_c and not sorting:
                sortAlgo = combSort
                algoID = "Comb"
            elif event.key == pg.K_y and not sorting:
                sortAlgo = cycleSort
                algoID = "Cycle"
            elif event.key == pg.K_j and not sorting:
                sortAlgo = timSort
                algoID = "Tim"
    pg.quit()


if __name__ == '__main__':
    main()
