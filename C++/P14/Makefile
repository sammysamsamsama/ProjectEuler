CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt

solution: P14.cpp
	 $(CXX) $(CXXFLAGS) P14.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

