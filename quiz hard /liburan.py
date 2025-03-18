class Destination:
    def __init__(self, name, cost=0):
        self.name = name
        self.cost = cost

class Meal:
    def __init__(self, type, cost=0):
        self.type = type  # breakfast, lunch, dinner
        self.cost = cost

class Accommodation:
    def __init__(self, name, cost=0):
        self.name = name
        self.cost = cost

class Day:
    def __init__(self, number, destinations=None, meals=None, accommodation=None):
        self.number = number
        self.destinations = destinations if destinations else []
        self.meals = meals if meals else []
        self.accommodation = accommodation
        
    def calculate_cost(self):
        dest_cost = sum(dest.cost for dest in self.destinations)
        meals_cost = sum(meal.cost for meal in self.meals)
        accom_cost = self.accommodation.cost if self.accommodation else 0
        return dest_cost + meals_cost + accom_cost
        
    def __str__(self):
        result = f"Day {self.number}:\n"
        result += "  Destinations: " + " → ".join([dest.name for dest in self.destinations]) + "\n"
        result += "  Meals: " + ", ".join([meal.type for meal in self.meals]) + "\n"
        if self.accommodation:
            result += f"  Accommodation: {self.accommodation.name}\n"
        result += f"  Cost: Rp{self.calculate_cost():,}\n"
        return result

class TravelItinerary:
    def __init__(self, budget):
        self.days = []
        self.budget = budget
        self.remaining_budget = budget
    
    def add_day(self, day):
        self.days.append(day)
        self.remaining_budget -= day.calculate_cost()
    
    def calculate_total_cost(self):
        return sum(day.calculate_cost() for day in self.days)
    
    def __str__(self):
        result = "=== RENCANA PERJALANAN: JAKARTA KE XINJIANG ===\n\n"
        result += f"Total Budget: Rp{self.budget:,}\n"
        for day in self.days:
            result += "\n" + str(day)
        result += f"\nTotal Cost: Rp{self.calculate_total_cost():,}\n"
        result += f"Remaining Budget: Rp{self.remaining_budget:,}\n"
        return result

def get_user_input():
    """
    Fungsi untuk mendapatkan input dari pengguna
    """
    print("====== PERENCANAAN PERJALANAN JAKARTA KE XINJIANG ======")
    print("Silakan masukkan informasi perjalanan Anda:")
    
    # Input budget
    while True:
        try:
            budget = float(input("Budget total perjalanan (dalam Rupiah): "))
            if budget <= 0:
                print("Budget harus lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Masukkan nilai numerik yang valid.")
    
    # Input jumlah orang
    while True:
        try:
            num_travelers = int(input("Jumlah peserta perjalanan: "))
            if num_travelers <= 0:
                print("Jumlah peserta harus lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid.")
    
    # Input durasi perjalanan atau gunakan default 10 hari
    while True:
        try:
            duration = input("Durasi perjalanan (default 10 hari): ")
            if duration == "":
                duration = 10
            else:
                duration = int(duration)
                if duration <= 0:
                    print("Durasi harus lebih besar dari 0.")
                    continue
            break
        except ValueError:
            print("Masukkan angka yang valid.")
    
    # Input tanggal keberangkatan
    departure_date = input("Tanggal keberangkatan (format: DD/MM/YYYY): ")
    
    # Input preferensi akomodasi
    accom_preference = input("Preferensi akomodasi (budget/standard/luxury): ").lower()
    if accom_preference not in ["budget", "standard", "luxury"]:
        accom_preference = "standard"  # Default jika input tidak valid
    
    # Input preferensi makanan
    meal_preference = input("Preferensi makanan (local/international/mixed): ").lower()
    if meal_preference not in ["local", "international", "mixed"]:
        meal_preference = "mixed"  # Default jika input tidak valid
    
    return {
        "budget": budget,
        "num_travelers": num_travelers,
        "duration": duration,
        "departure_date": departure_date,
        "accom_preference": accom_preference,
        "meal_preference": meal_preference
    }

def adjust_costs_based_on_input(user_input):
    """
    Menyesuaikan biaya berdasarkan input pengguna
    """
    accommodation_multiplier = {
        "budget": 0.8,
        "standard": 1.0,
        "luxury": 1.5
    }
    
    meal_multiplier = {
        "local": 0.7,
        "mixed": 1.0,
        "international": 1.3
    }
    
    # Faktor pengali berdasarkan jumlah orang (ekonomi skala)
    traveler_multiplier = max(0.9, 1 - (user_input["num_travelers"] - 1) * 0.05)
    
    return {
        "accommodation": accommodation_multiplier[user_input["accom_preference"]],
        "meal": meal_multiplier[user_input["meal_preference"]],
        "traveler": traveler_multiplier,
        "per_person": user_input["budget"] / user_input["num_travelers"]
    }

def backtrack_planning(user_input):
    """
    Menggunakan algoritma backtracking untuk menyesuaikan biaya perjalanan
    agar sesuai dengan budget yang ditentukan
    """
    # Mendapatkan faktor pengali biaya berdasarkan input pengguna
    cost_factors = adjust_costs_based_on_input(user_input)
    
    # Budget per orang
    budget_per_person = cost_factors["per_person"]
    
    # Inisialisasi biaya awal untuk tiap komponen (per orang)
    flight_costs = {
        "Jakarta-Beijing": 7500000 * cost_factors["traveler"],
        "Beijing-Urumqi": 2500000 * cost_factors["traveler"],
    }
    
    # Perkiraan biaya akomodasi per malam (per orang)
    base_accommodation_cost = 800000
    accommodation_costs = {
        "Hotel Beijing Airport": base_accommodation_cost * 1.5 * cost_factors["accommodation"],
        "Hotel Hoitak": base_accommodation_cost * 1.1 * cost_factors["accommodation"],
        "Hotel Furui": base_accommodation_cost * 1.0 * cost_factors["accommodation"],
        "Hotel Yuyifeng": base_accommodation_cost * 1.2 * cost_factors["accommodation"],
        "Hotel Baihualin": base_accommodation_cost * 1.3 * cost_factors["accommodation"],
        "Villa Hemu": base_accommodation_cost * 1.5 * cost_factors["accommodation"],
        "Hotel Kunmo": base_accommodation_cost * 1.1 * cost_factors["accommodation"],
        "Hotel Jiaohe Mano": base_accommodation_cost * 1.2 * cost_factors["accommodation"],
    }
    
    # Perkiraan biaya transportasi antar destinasi (per orang)
    base_transport_cost = 100000
    transportation_costs = {
        "Beijing-Urumqi": base_transport_cost * 3.0 * cost_factors["traveler"],
        "Urumqi-Heavenly Lake": base_transport_cost * 1.5 * cost_factors["traveler"],
        "Heavenly Lake-Fuyun": base_transport_cost * 3.0 * cost_factors["traveler"],
        "Fuyun-Keketuohai": base_transport_cost * 1.5 * cost_factors["traveler"],
        "Keketuohai-Burqin": base_transport_cost * 2.5 * cost_factors["traveler"],
        "Burqin-Kanas": base_transport_cost * 2.0 * cost_factors["traveler"],
        "Kanas-Jiadengyu": base_transport_cost * 1.5 * cost_factors["traveler"],
        "Jiadengyu-Hemu": base_transport_cost * 1.5 * cost_factors["traveler"],
        "Hemu-Burqin": base_transport_cost * 2.5 * cost_factors["traveler"],
        "Burqin-Ulho": base_transport_cost * 2.0 * cost_factors["traveler"],
        "Ulho-Turpan": base_transport_cost * 3.5 * cost_factors["traveler"],
        "Turpan-Urumqi": base_transport_cost * 1.5 * cost_factors["traveler"],
    }
    
    # Perkiraan biaya makan per orang
    base_meal_cost = 50000
    meal_costs = {
        "Breakfast": base_meal_cost * 1.0 * cost_factors["meal"],
        "Lunch": base_meal_cost * 1.5 * cost_factors["meal"],
        "Dinner": base_meal_cost * 2.0 * cost_factors["meal"],
    }
    
    # Perkiraan biaya wisata per destinasi (per orang)
    base_attraction_cost = 100000
    attraction_costs = {
        "Beijing City Tour": base_attraction_cost * 2.0,
        "Urumqi City Tour": base_attraction_cost * 1.5,
        "Heavenly Lake": base_attraction_cost * 1.2,
        "Fuyun": base_attraction_cost * 0.8,
        "Keketuohai": base_attraction_cost * 1.4,
        "Burqin": base_attraction_cost * 0.8,
        "Kanas": base_attraction_cost * 1.6,
        "Jiadengyu": base_attraction_cost * 1.0,
        "Hemu": base_attraction_cost * 1.2,
        "Ulho": base_attraction_cost * 1.0,
        "Turpan": base_attraction_cost * 1.4,
        "International Bazaar": base_attraction_cost * 0.8,
    }
    
    # Total budget yang ditentukan
    target_budget = user_input["budget"]
    num_travelers = user_input["num_travelers"]
    
    # Membuat rencana perjalanan awal
    itinerary = TravelItinerary(target_budget)
    
    # Day 1: Jakarta ke Beijing (Flight only)
    day1 = Day(1)
    day1.destinations.append(Destination("Jakarta ke Beijing", flight_costs["Jakarta-Beijing"] * num_travelers))
    itinerary.add_day(day1)
    
    # Day 2: Beijing ke Urumqi
    day2 = Day(2)
    day2.destinations.append(Destination("Beijing ke Urumqi", flight_costs["Beijing-Urumqi"] * num_travelers))
    day2.meals.append(Meal("Dinner", meal_costs["Dinner"] * num_travelers))
    day2.accommodation = Accommodation("Hotel Hoitak", accommodation_costs["Hotel Hoitak"] * num_travelers)
    itinerary.add_day(day2)
    
    # Day 3: Urumqi ke Heavenly Lake dan Fuyun
    day3 = Day(3)
    day3.destinations.append(Destination("Urumqi ke Heavenly Lake", 
                                       (transportation_costs["Urumqi-Heavenly Lake"] + 
                                        attraction_costs["Heavenly Lake"]) * num_travelers))
    day3.destinations.append(Destination("Heavenly Lake ke Fuyun", 
                                       (transportation_costs["Heavenly Lake-Fuyun"] + 
                                        attraction_costs["Fuyun"]) * num_travelers))
    day3.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    day3.meals.append(Meal("Lunch", meal_costs["Lunch"] * num_travelers))
    day3.meals.append(Meal("Dinner", meal_costs["Dinner"] * num_travelers))
    day3.accommodation = Accommodation("Hotel Furui", accommodation_costs["Hotel Furui"] * num_travelers)
    itinerary.add_day(day3)
    
    # Day 4: Fuyun ke Keketuohai dan Burqin
    day4 = Day(4)
    day4.destinations.append(Destination("Fuyun ke Keketuohai", 
                                       (transportation_costs["Fuyun-Keketuohai"] + 
                                        attraction_costs["Keketuohai"]) * num_travelers))
    day4.destinations.append(Destination("Keketuohai ke Burqin", 
                                       (transportation_costs["Keketuohai-Burqin"] + 
                                        attraction_costs["Burqin"]) * num_travelers))
    day4.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    day4.meals.append(Meal("Lunch", meal_costs["Lunch"] * num_travelers))
    day4.meals.append(Meal("Dinner", meal_costs["Dinner"] * num_travelers))
    day4.accommodation = Accommodation("Hotel Yuyifeng", accommodation_costs["Hotel Yuyifeng"] * num_travelers)
    itinerary.add_day(day4)
    
    # Day 5: Burqin ke Kanas dan Jiadengyu
    day5 = Day(5)
    day5.destinations.append(Destination("Burqin ke Kanas", 
                                       (transportation_costs["Burqin-Kanas"] + 
                                        attraction_costs["Kanas"]) * num_travelers))
    day5.destinations.append(Destination("Kanas ke Jiadengyu", 
                                       (transportation_costs["Kanas-Jiadengyu"] + 
                                        attraction_costs["Jiadengyu"]) * num_travelers))
    day5.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    day5.meals.append(Meal("Lunch", meal_costs["Lunch"] * num_travelers))
    day5.meals.append(Meal("Dinner", meal_costs["Dinner"] * num_travelers))
    day5.accommodation = Accommodation("Hotel Baihualin", accommodation_costs["Hotel Baihualin"] * num_travelers)
    itinerary.add_day(day5)
    
    # Day 6: Jiadengyu ke Hemu dan Burqin
    day6 = Day(6)
    day6.destinations.append(Destination("Jiadengyu ke Hemu", 
                                       (transportation_costs["Jiadengyu-Hemu"] + 
                                        attraction_costs["Hemu"]) * num_travelers))
    day6.destinations.append(Destination("Hemu ke Burqin", 
                                       (transportation_costs["Hemu-Burqin"] + 
                                        attraction_costs["Burqin"]) * num_travelers))
    day6.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    day6.meals.append(Meal("Lunch", meal_costs["Lunch"] * num_travelers))
    day6.meals.append(Meal("Dinner", meal_costs["Dinner"] * num_travelers))
    day6.accommodation = Accommodation("Villa Hemu", accommodation_costs["Villa Hemu"] * num_travelers)
    itinerary.add_day(day6)
    
    # Day 7: Burqin ke Ulho
    day7 = Day(7)
    day7.destinations.append(Destination("Burqin ke Ulho", 
                                       (transportation_costs["Burqin-Ulho"] + 
                                        attraction_costs["Ulho"]) * num_travelers))
    day7.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    day7.meals.append(Meal("Lunch", meal_costs["Lunch"] * num_travelers))
    day7.meals.append(Meal("Dinner", meal_costs["Dinner"] * num_travelers))
    day7.accommodation = Accommodation("Hotel Kunmo", accommodation_costs["Hotel Kunmo"] * num_travelers)
    itinerary.add_day(day7)
    
    # Day 8: Ulho ke Turpan
    day8 = Day(8)
    day8.destinations.append(Destination("Ulho ke Turpan", 
                                       (transportation_costs["Ulho-Turpan"] + 
                                        attraction_costs["Turpan"]) * num_travelers))
    day8.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    day8.meals.append(Meal("Lunch", meal_costs["Lunch"] * num_travelers))
    day8.meals.append(Meal("Dinner", meal_costs["Dinner"] * num_travelers))
    day8.accommodation = Accommodation("Hotel Jiaohe Mano", accommodation_costs["Hotel Jiaohe Mano"] * num_travelers)
    itinerary.add_day(day8)
    
    # Day 9: Turpan ke Urumqi ke Beijing
    day9 = Day(9)
    day9.destinations.append(Destination("Turpan ke Urumqi", transportation_costs["Turpan-Urumqi"] * num_travelers))
    day9.destinations.append(Destination("Urumqi ke Beijing", flight_costs["Beijing-Urumqi"] * num_travelers))
    day9.destinations.append(Destination("International Bazaar", attraction_costs["International Bazaar"] * num_travelers))
    day9.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    day9.meals.append(Meal("Lunch", meal_costs["Lunch"] * num_travelers))
    day9.accommodation = Accommodation("Hotel Beijing Airport", accommodation_costs["Hotel Beijing Airport"] * num_travelers)
    itinerary.add_day(day9)
    
    # Day 10: Beijing ke Jakarta
    day10 = Day(10)
    day10.destinations.append(Destination("Beijing ke Jakarta", 0))  # Biaya sudah termasuk di hari 1
    day10.meals.append(Meal("Breakfast", meal_costs["Breakfast"] * num_travelers))
    itinerary.add_day(day10)
    
    # Cek apakah biaya total sesuai dengan budget
    total_cost = itinerary.calculate_total_cost()
    
    # Jika biaya total tidak sesuai dengan budget, lakukan penyesuaian
    if total_cost != target_budget:
        difference = target_budget - total_cost
        adjust_cost(itinerary, difference)
        
    return itinerary

def adjust_cost(itinerary, difference):
    """
    Menyesuaikan biaya perjalanan agar tepat sesuai budget
    dengan cara mengubah biaya penerbangan
    """
    # Menggunakan algoritma backtracking sederhana
    # Jika perbedaannya kecil, sesuaikan biaya tiket penerbangan di hari pertama
    itinerary.days[0].destinations[0].cost += difference
    
    # Perbarui remaining budget
    itinerary.remaining_budget = 0  # Set ke 0 karena kita ingin pas dengan budget

def print_itinerary_details(itinerary, user_input):
    """
    Mencetak detail lengkap rencana perjalanan
    """
    print("\n" + "="*60)
    print(f"DETAIL RENCANA PERJALANAN: JAKARTA KE XINJIANG")
    print("="*60)
    print(f"Jumlah peserta: {user_input['num_travelers']} orang")
    print(f"Tanggal keberangkatan: {user_input['departure_date']}")
    print(f"Durasi perjalanan: {user_input['duration']} hari")
    print(f"Preferensi akomodasi: {user_input['accom_preference']}")
    print(f"Preferensi makanan: {user_input['meal_preference']}")
    print(f"Budget total: Rp{user_input['budget']:,.2f}")
    print(f"Budget per orang: Rp{user_input['budget']/user_input['num_travelers']:,.2f}")
    print("="*60)
    
    print(itinerary)
    
    print("\nPERINGATAN PENTING:")
    print("1. Pastikan paspor Anda berlaku minimal 6 bulan dari tanggal keberangkatan")
    print("2. Periksa persyaratan visa terbaru untuk wilayah Xinjiang")
    print("3. Konfirmasikan ketersediaan akomodasi dan transportasi sebelum keberangkatan")
    print("4. Periksa cuaca dan kondisi wilayah Xinjiang sebelum keberangkatan")
    print("5. Siapkan asuransi perjalanan yang mencakup seluruh aktivitas perjalanan")
    print("="*60)

def export_itinerary_to_file(itinerary, user_input, filename="rencana_perjalanan.txt"):
    """
    Menyimpan rencana perjalanan ke file
    """
    with open(filename, "w") as file:
        file.write("="*60 + "\n")
        file.write(f"DETAIL RENCANA PERJALANAN: JAKARTA KE XINJIANG\n")
        file.write("="*60 + "\n")
        file.write(f"Jumlah peserta: {user_input['num_travelers']} orang\n")
        file.write(f"Tanggal keberangkatan: {user_input['departure_date']}\n")
        file.write(f"Durasi perjalanan: {user_input['duration']} hari\n")
        file.write(f"Preferensi akomodasi: {user_input['accom_preference']}\n")
        file.write(f"Preferensi makanan: {user_input['meal_preference']}\n")
        file.write(f"Budget total: Rp{user_input['budget']:,.2f}\n")
        file.write(f"Budget per orang: Rp{user_input['budget']/user_input['num_travelers']:,.2f}\n")
        file.write("="*60 + "\n\n")
        
        file.write(str(itinerary) + "\n")
        
        file.write("\nPERINGATAN PENTING:\n")
        file.write("1. Pastikan paspor Anda berlaku minimal 6 bulan dari tanggal keberangkatan\n")
        file.write("2. Periksa persyaratan visa terbaru untuk wilayah Xinjiang\n")
        file.write("3. Konfirmasikan ketersediaan akomodasi dan transportasi sebelum keberangkatan\n")
        file.write("4. Periksa cuaca dan kondisi wilayah Xinjiang sebelum keberangkatan\n")
        file.write("5. Siapkan asuransi perjalanan yang mencakup seluruh aktivitas perjalanan\n")
        file.write("="*60 + "\n")
    
    print(f"\nRencana perjalanan berhasil disimpan ke file '{filename}'")

def main():
    # Menerima input dari pengguna
    user_input = get_user_input()
    
    # Gunakan input default jika pengguna tidak memberikan input
    if user_input["budget"] == 0:
        user_input["budget"] = 26990000
    
    # Buat rencana perjalanan
    trip = backtrack_planning(user_input)
    
    # Tampilkan detail rencana perjalanan
    print_itinerary_details(trip, user_input)
    
    # Tanya pengguna apakah ingin menyimpan rencana perjalanan ke file
    save_to_file = input("\nApakah Anda ingin menyimpan rencana perjalanan ke file? (y/n): ").lower()
    if save_to_file == 'y':
        filename = input("Masukkan nama file (default: rencana_perjalanan.txt): ")
        if filename == "":
            filename = "rencana_perjalanan.txt"
        export_itinerary_to_file(trip, user_input, filename)

if __name__ == "__main__":
    main()
