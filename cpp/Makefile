all: default

CXXFLAGS =	-O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP 
OBJS = 

START_DIR=$(PWD)
BASE_DIR=$(PWD)
BUILD_DIR=$(BASE_DIR)/build/linux

clean:
	rm -rf $(BUILD_DIR)/*

default:
	@mkdir -p $(BUILD_DIR)
	$(CXX) -o $(BUILD_DIR)/akseed_calc main.cpp -std=c++11