from itertools import combinations

weight_items = [1, 2, 4, 8, 16, 32, 64, 128, 128*2]
len_weight = len(weight_items)
#target_weight_list = [18, 24, 22, 48]
target_weight_list = [14,8,8,30,1024]

prev_weight_history = []
accum_energey = 0
for target_weight in target_weight_list:
    result = []
    for i in range(2, len_weight):
        comb_list = list(combinations(weight_items, i))
        for new_item in comb_list:
            new_item = list(new_item)
            new_item.sort(reverse=True)

            side_weight = int(target_weight/2)
            sum_item_weight = sum(new_item)

            if sum_item_weight == side_weight:
                if len(prev_weight_history) == 0: #처음의 경우
                    prev_weight_history = new_item #신규 항목추가
                    new_energy = sum(new_item) * 2
                else:
                    if prev_weight_history[0] >= new_item[0]:
                        diffence = set(prev_weight_history)^set(new_item) #part replace
                        new_energy = sum(diffence) * 2
                    else:
                        new_energy = sum(prev_weight_history + new_item) * 2
                    prev_weight_history = new_item #whole reset
                accum_energey += new_energy
                print(f"목표 무계 {target_weight}, New item {new_item}, 소모 에너지 : {new_energy}, ")
                print(accum_energey)
                i = len_weight
                break