class Solution:
    def asteroidCollision(self, asteroids: list) -> list:

        man_idx = 0

        while man_idx < len(asteroids):
            if asteroids[man_idx] > 0:
                if man_idx == len(asteroids)-1:
                    break
                elif asteroids[man_idx+1] + asteroids[man_idx] > 0 and asteroids[man_idx+1] < 0:
                    asteroids.pop(man_idx+1)
                elif asteroids[man_idx+1] + asteroids[man_idx] == 0:
                    asteroids.pop(man_idx)
                    asteroids.pop(man_idx)
                elif asteroids[man_idx+1] + asteroids[man_idx] < 0:
                    asteroids.pop(man_idx)
                else:
                    man_idx += 1
            elif asteroids[man_idx] < 0:
                if man_idx == 0:
                    man_idx += 1
                elif asteroids[man_idx-1] + asteroids[man_idx] > 0:
                    asteroids.pop(man_idx)
                elif asteroids[man_idx-1] + asteroids[man_idx] == 0:
                    asteroids.pop(man_idx-1)
                    asteroids.pop(man_idx-1)
                    man_idx -= 1
                elif asteroids[man_idx-1] + asteroids[man_idx] < 0 and asteroids[man_idx-1] > 0:
                    asteroids.pop(man_idx-1)
                    man_idx -= 1
                else:
                    man_idx += 1

            
        return asteroids