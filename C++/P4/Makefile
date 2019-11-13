CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: test

test: P4.cpp
	 $(CXX) $(CXXFLAGS) P4.cpp -o test

clean:
	-rm -f *.o *.gch *~ a.out test *.txt

