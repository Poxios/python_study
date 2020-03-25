def timer(h, m, s):  # Timer Function
    print("10초 간격으로 프린트 됩니다.")
    while True:
        # Notice time left
        if s % 10 == 0:
            print(str(h) + "시간", str(m) + "분", str(s) + "초 남았습니다.")

        # Breaking timimg
        if h == 0 and m == 0 and s == 0:
            print("시작합니다")
            break

        # Time going
        if s == 0:
            if m == 0:
                h -= 1
                m = 59
                s = 59
            else:
                m -= 1
                s = 59
        else:
            s -= 1

        # One second
        time.sleep(1)

    return 0
