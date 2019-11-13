CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: test

test: P1.cpp
	 $(CXX) $(CXXFLAGS) P1.cpp -o test

clean:
	-rm -f *.o *.gch *~ a.out test *.txt

