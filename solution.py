from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Функция возвращает минимальную длину подмассива в массиве `nums`,
        сумма которого больше или равна `target`.
        
        Используется паттерн siding window с переменным размером окна.
        left - индекс элемента начала siding window
        right - индекс элемента конца siding window
        siding window и есть подмассив сумму элементов в котором мы отслеживаем.
        
        Если сумма чисел в siding window < target - сдвигаем right вправо
        Если сумма чисел в siding window >= target, то
        1) если left < right, - сдвигаем left вправо
        2) если left == right, - сдвигаем right вправо, чтобы начало не обогнало конец окна
        
        Временная сложность O(n) - в худшем случае оба указателя пройдут весь массив по одному разу.
        Пространственная сложность O(1) - память на доп. константы
        
        Args:
            target (int): порог по сумме элементов подмассива, который мы ищем
            nums (List[int]): массив положительных целых чисел

        Returns:
            int: минимальная длина подмассива, сумма которого больше или равна порогу `target`
        """
        left = 0
        right = 0
        window_sum = nums[0]
        window_len = 1
        min_window_len = len(nums) + 1

        while right < len(nums):
            if window_sum < target:
                right += 1

                if right == len(nums):
                    break

                window_sum += nums[right]
            else:
                window_len = right - left + 1

                if window_len < min_window_len:
                    min_window_len = window_len

                if left < right:
                    window_sum -= nums[left]
                    left += 1
                else:
                    right += 1

                    if right == len(nums):
                        break

                    window_sum += nums[right]

        # Если такого подмассива нет, верните 0.
        if min_window_len == len(nums) + 1:
            min_window_len = 0

        return min_window_len
