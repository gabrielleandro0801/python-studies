import time


def make_burger(order_num):
    print(f"Preparing burger #{order_num}...")
    time.sleep(5)
    print(f"Burger made #{order_num}")


def main():
    for i in range(3):
        make_burger(i)


if __name__ == "__main__":
    # This code is run synchronously, where each burger is made after the previous one
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Orders completed in {elapsed:0.2f} seconds.")
