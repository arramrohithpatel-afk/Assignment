def calculate_ticket_price(seats, timing, is_weekend):
    
    prices = {
        "VIP": 500,
        "REGULAR": 300,
        "ECONOMY": 150
    }

    timing_multiplier = {
        "morning": 0.8,
        "afternoon": 1,
        "evening": 1.2,
        "night": 1.5
    }

    print("Seats:", seats)
    print("Timing:", timing)
    print("Weekend:", is_weekend)

    # Filter valid seats
    valid_seats = [s for s in seats if s in prices]

    if len(valid_seats) == 0:
        return "No valid booking"

    print("\nValid Seats:", valid_seats)

    # 1. Base total
    base_total = sum(prices[s] for s in valid_seats)
    print("\n1. Base Total:", base_total)

    # 2. Timing adjustment
    timing_total = base_total * timing_multiplier[timing]
    print("2. After Timing Adjustment:", timing_total)

    # 3. Weekend surcharge
    if is_weekend:
        weekend_extra = timing_total * 0.10
        timing_total += weekend_extra
        print("3. Weekend Added:", weekend_extra)
    else:
        print("3. No Weekend Charge")

    print("After Weekend:", timing_total)

    # 4. Bulk discount
    discount = 0
    if len(valid_seats) >= 5:
        discount = timing_total * 0.15
        timing_total -= discount
        print("4. Bulk Discount Applied:", discount)
    else:
        print("4. No Bulk Discount")

    print("After Discount:", timing_total)

    # 5. Booking fee
    booking_fee = 50 * len(valid_seats)
    total_with_fee = timing_total + booking_fee
    print("\n5. Booking Fee:", booking_fee)
    print("After Fee:", total_with_fee)

    # 6. GST
    tax = total_with_fee * 0.12
    print("\n6. GST (12%):", tax)

    # 7. Final amount
    final_amount = round(total_with_fee + tax)
    print("\n7. Final Amount:", final_amount)

    return {
        "base_total": base_total,
        "timing_adjustment": round(timing_total),
        "discount": round(discount),
        "tax": round(tax),
        "final_amount": final_amount
    }


# 🔹 Example Run
result = calculate_ticket_price(
    ["VIP", "REGULAR", "VIP"],
    "evening",
    True
)

print("\nFinal Output:", result)