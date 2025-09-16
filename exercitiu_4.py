
class NumberProcesor:

    def split_list(self, numbers):
       sorted_num = sorted(numbers)
       mid = len(sorted_num) // 2
       small = sorted_num[:mid]
       large = sorted_num[mid:]
       return small, large

    def sorted_even_numbers(self, numbers):
        sorted_num = []
        for num in numbers:
            if num % 2 == 0:
                sorted_num.append(num)
        return sorted(sorted_num)

    def sum_and_average(self, numbers):
        total = sum(numbers)
        avg = total/ len(numbers)
        return(total, avg)

    def numbers_squared(self, numbers):
        resultat = []
        for nums in numbers:
            resultat.append((nums,nums ** 2))
        return resultat

    def multiply_all(self, numbers, factor):
        result = []
        for num in numbers:
          result.append(num * factor)
        return result

num = [787, 390, 949, 573, 738, 606, 566, 213, 226,
       125, 974, 936, 625, 290, 584, 472, 295, 995, 759,
       129, 679, 425, 960, 138, 659, 213, 717, 205, 126,
       479]

processor = NumberProcesor()

small, large = processor.split_list(num)
print(small)
print(large)

print(processor.sorted_even_numbers(num))
print(processor.sum_and_average(num))
print(processor.numbers_squared(num))
print(processor.multiply_all(num, 1))
