# 1. sep 구분자
print('S','E','P', sep='@')   # S@E@P

# 2. end 줄바꿈X
print("I like", end=" @ ")    # I like @ money
print("money")

# 3. string format method
%d int $f float %s string
print("%s을 %d개 주세요." % ("아이스크림", 10))          # 아이스크림을 10개 주세요
print("{0}을 {1}개 주세요.".format("아이스크림", 10))    # 아이스크림을 10개 주세요

# 4. Escape
\n \t 
\\ \' \" 출력
print("역슬래쉬\\, 따옴표\', 쌍따옴표\"")