n, m, a, b = map(int, input().split())

single_ticket_price = a
multi_ticket_price = b
rides_needed = n
rides_per_pass = m

full_passes = rides_needed // rides_per_pass
leftover_pass = rides_needed % rides_per_pass

leftover_cost = min(leftover_pass*single_ticket_price, multi_ticket_price)
total_cost = (full_passes * multi_ticket_price) + leftover_cost 


single_cost = rides_needed * single_ticket_price


print(min(total_cost, single_cost))

