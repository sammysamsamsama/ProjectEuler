CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution

solution: P7.cpp
	 $(CXX) $(CXXFLAGS) P7.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

