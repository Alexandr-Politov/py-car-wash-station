class Car:
    def __init__(self,
                 comfort_class: int = 1,
                 clean_mark: int = 1,
                 brand: str = ""):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float = 1.0,
                 clean_power: int = 1,
                 average_rating: float = 1.0,
                 count_of_ratings: int = 0):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        washing_price = ((car.comfort_class *
                         (self.clean_power - car.clean_mark) *
                         self.average_rating) /
                         self.distance_from_city_center)
        return round(washing_price, 1)

    def wash_single_car(self, car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> float:
        old_rating = self.average_rating * self.count_of_ratings
        new_rating = old_rating + rating
        self.count_of_ratings += 1
        self.average_rating = round(new_rating / self.count_of_ratings, 1)
        return self.average_rating

    def serve_cars (self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)
