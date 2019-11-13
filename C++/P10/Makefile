CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt

solution: P10.cpp
	 $(CXX) $(CXXFLAGS) P10.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

