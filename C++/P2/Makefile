CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: test

test: P2.cpp
	 $(CXX) $(CXXFLAGS) P2.cpp -o test

clean:
	-rm -f *.o *.gch *~ a.out test *.txt

