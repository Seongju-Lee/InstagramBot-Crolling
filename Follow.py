class Follow:

    def Follow_func(self):
        time.sleep(2)
    if finish_like == False:
        first_post = driver.find_elements_by_xpath('//div[1]/div/div/div[1]/div[1]/a')[0]
        first_post.click()
        finish_like = True
    list_ = []

    button_list = driver.find_elements_by_xpath("//button")

    for i in button_list: # 닉네임인지 확인 팔로우 부분
        list_.append(i.text)

        for j in range(len(list_)):
            
            if list_[j] == '팔로잉':
                print(list_[j])
                bool_following = True
                break
            else:
                bool_following = False


    time.sleep(2)

    if bool_following == True:
        element_list = driver.find_elements_by_xpath("//a") # a태그 찾음 다음 부분
        for j in element_list:
            if j.text == '다음':
                A.add_one()
                # Global_var.num += 1
                bool_ = False
                j.click()
                break


    elif bool_following == False:

        follow = driver.find_elements_by_xpath('//div[2]/div[1]/div[1]/span/a')[0]
        follow.click()

        # 팔로우 부분
        button_list = driver.find_elements_by_xpath("//button") # button 태그 찾음
        for i in button_list: # 닉네임인지 확인
            if i.text == '팔로우':
                follow_button = driver.find_elements_by_xpath('//div/span/span[1]/button')[0]
                follow_button.click()
                finish_like = False
                break
        
        print(num)
        # driver.get(current_url)
        for _ in range(num + 2):
            driver.back()
        
        
        bool_ = True