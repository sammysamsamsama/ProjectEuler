CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt

solution: P9.cpp
	 $(CXX) $(CXXFLAGS) P9.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

